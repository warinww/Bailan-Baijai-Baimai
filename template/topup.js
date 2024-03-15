async function get_channels() {
    const response = await axios.get(`http://127.0.0.1:8000/channels`);
    console.log(response.data);
    const channel = response.data['channels'];
    displaychannels(channel);
    console.log(channel)
  }
  
  function displaychannels(channels) {
    const payment_channel = document.getElementById('channels');
    payment_channel.innerHTML = ``;
  
    channels.forEach(channel => {
      const div = document.createElement('div');
      div.innerHTML = `<p>${channel.id} ${channel.name}</p>`;
      payment_channel.appendChild(div);
    });
  }
  