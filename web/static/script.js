const form = document.getElementById("predictionForm");
const result = document.getElementById("result");
const errorBox = document.getElementById("error");
const priceElement = document.getElementById("price");
const predictButton = document.querySelector(".predict-btn");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    // Hide previous messages
    result.classList.add("hidden");
    errorBox.classList.add("hidden");

    // Get button elements
    const buttonText = predictButton.querySelector("span:first-child");
    const arrow = predictButton.querySelector(".arrow");

    // Loading state
    buttonText.textContent = "Predicting...";
    arrow.textContent = "⏳";
    predictButton.disabled = true;

    // Collect form values
    const data = {
        house_size_sqft: document.getElementById("house_size_sqft").value,
        bedrooms: document.getElementById("bedrooms").value,
        bathrooms: document.getElementById("bathrooms").value,
        age_years: document.getElementById("age_years").value,
        distance_to_city_km:
            document.getElementById("distance_to_city_km").value,
        parking_spaces: document.getElementById("parking_spaces").value
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const resultData = await response.json();

        if (!response.ok || !resultData.success) {
            throw new Error(
                resultData.error || "Unable to generate prediction."
            );
        }

        // Format price in Indian currency
        const formattedPrice = new Intl.NumberFormat("en-IN", {
            style: "currency",
            currency: "INR",
            maximumFractionDigits: 0
        }).format(resultData.predicted_price);

        priceElement.textContent = formattedPrice;

        // Show result
        result.classList.remove("hidden");

    } catch (error) {
        errorBox.textContent =
            "Prediction failed: " + error.message;

        errorBox.classList.remove("hidden");

    } finally {
        // Restore button
        buttonText.textContent = "Predict House Price";
        arrow.textContent = "→";
        predictButton.disabled = false;
    }
});