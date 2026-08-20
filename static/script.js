function sendMessage() {
    const text = document.getElementById("userInput").value;

    fetch("/api/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.reply;
    });
}
