document.getElementById("sendBtn").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function(e){
    if(e.key === "Enter") sendMessage();
});

async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if(!message) return;

    addMessage(message, "user");
    input.value = "";

    try {
        const res = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        });
        const data = await res.json();
        addMessage(data.reply, "bot");
    } catch(err) {
        addMessage("❌ Server error", "bot");
        console.error(err);
    }
}

function addMessage(text, sender) {
    const chatBox = document.getElementById("chatBox");
    const div = document.createElement("div");
    div.className = sender;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}
