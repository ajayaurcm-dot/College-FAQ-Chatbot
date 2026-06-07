export default async function sendMessage(message: string) {
  try {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: message,        // ✅ FIXED
        session_id: "user_1"   // ✅ REQUIRED
      }),
    });

    const data = await res.json();
    return data.answer;  // ⚠️ also changed from reply → answer

  } catch {
    return "Server not reachable.";
  }
}