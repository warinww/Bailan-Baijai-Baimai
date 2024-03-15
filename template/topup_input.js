
async function top_up(event) {
    event.preventDefault();
    const money = document.getElementById('money').value;
    const account_id = localStorage.getItem('account_id');
    const channel = document.getElementById('channel').value;
    console.log("Money:", money);
    console.log("Channel:", channel);

    try {
        const response = await axios.post(`http://127.0.0.1:8000/top_up?account_id=${account_id}&channel_id=${channel}`, {
            "coin": money,
        });
        console.log("Response:", response);
        
         alert(response.data.status);
    } catch (error) {
        console.error("Error:", error);
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Pleas increse/decrese 1 Baht!",
          });
    }
}
document.getElementById('topUpButton').addEventListener('click', top_up);
