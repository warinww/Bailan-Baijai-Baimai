async function addToCart() {
    const queryParams = new URLSearchParams(window.location.search);
    const bookId = queryParams.get('id');
    const accountId = localStorage.getItem('account_id');
    try {
        const response = await axios.post(`http://127.0.0.1:8000/add_cart?reader_id=${accountId}&book_id=${bookId}`);
        // console.log(response.data.book)
        result = response.data.book
        console.log(result)
        if (result == "Success") {
            Swal.fire({
                icon: "success",
                title: "Book added to cart",
                showConfirmButton: false,
                timer: 1500
            });
            return;
        } else if (result == "Book is already in the cart"){
            Swal.fire({
                icon: "error",
                title: "Book is already in the cart",
                showConfirmButton: false,
                timer: 1500
            });
            return;
        } else if (result == "You already have this book"){
            Swal.fire({
                icon: "error",
                title: "You already have this book",
                showConfirmButton: false,
                timer: 1500
            });
            return;
        }
    } catch (error) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong!",
            footer: '<a href="#" style="text-align: center;">Why do I have this issue?</a>'
        });        
    }
}

function check_collection(accountType) {
    console.log(Type);
    if (accountType === Type) {
      window.location.href = 'reader_book_collection.html';
    } else {
      window.location.href = 'writer_book_collection.html';
    }
  }
  
  document.addEventListener('DOMContentLoaded', function () {
  
    // Check if there is a saved account ID
    if (account_id) {
        // Display the account ID on the page
        // document.getElementById('result').innerHTML = "Account ID: " + account_id;
  
        // Periodically update coin information using the retrieved account ID
        setInterval(function () {
            loadCoinInfo(account_id);
        }, 350); // Update every 5 seconds (adjust as needed)
    } else {
        // Handle the case where there is no saved account ID
        console.log("No account ID found in localStorage.");
    }
  });
  
  function loadCoinInfo(account_id) {
    // Make an AJAX request to fetch coin information using the account ID
    var xhr = new XMLHttpRequest();
  
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var result = JSON.parse(xhr.responseText);
            document.getElementById('result').innerHTML = "Coin: " + result.coin;
        }
    };
  
    // Adjust the URL to match your FastAPI route
    xhr.open("GET", "http://127.0.0.1:8000/search_coin?id=" + account_id, true);
    xhr.send();
  }