async function get_coin_transaction(account_id) {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/show_coin_transaction?ID=${account_id}`);
        const coinTransacList = response.data["Coin Transaction's List"];
        displayCoinTransac(coinTransacList);
    } catch (error) {
        console.error("Error fetching coin transaction history:", error);
        // Handle the error, display a message, or redirect the user as needed.
    }
}

function displayCoinTransac(coinTransacList) {
    const Cointrans = document.getElementById("cointrans");
    Cointrans.innerHTML = "";

    if (Array.isArray(coinTransacList) && coinTransacList.length > 0) {
        coinTransacList.forEach(info => {
            Cointrans.innerHTML += `<p>Transaction: ${info}</p>`;
        });
    } else {
        console.error("No or invalid coin transaction history found.");
        // Handle the case where no valid transaction history is available, e.g., display a message or redirect the user.
    }
}

async function get_payment_transaction(account_id) {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/show_payment_history?ID=${account_id}`);
        const paymentTransacList = response.data["Payment History's List"];
        displayPaymentTransac(paymentTransacList);
    } catch (error) {
        console.error("Error fetching coin transaction history:", error);
        // Handle the error, display a message, or redirect the user as needed.
    }
}

function displayPaymentTransac(paymentTransacList) {
    const Paymenttrans = document.getElementById("paymenttrans");
    Paymenttrans.innerHTML = "";

    if (Array.isArray(paymentTransacList) && paymentTransacList.length > 0) {
        paymentTransacList.forEach(data => {   
            Paymenttrans.innerHTML += `<p>Transaction: ${data}</p>`;
        });
    } else {
        console.error("No or invalid coin transaction history found.");
        // Handle the case where no valid transaction history is available, e.g., display a message or redirect the user.
    }
}