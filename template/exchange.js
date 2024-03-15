async function exchange(event) {
    event.preventDefault();
    const coin = document.getElementById('coin').value;
    const account_id = localStorage.getItem('account_id');
    console.log("Coin:", coin);
    console.log(account_id)
    
    try {
        const response = await axios.post(`http://127.0.0.1:8000/exchange?writer_id=${account_id}`, {
            "coin": coin
        });
        console.log("Response:", response);
        alert(response.data.status);
    } catch (error) {
        console.error("Error:", error);
        alert(error.response ? error.response.data.detail : 'An error occurred.');
    }
}