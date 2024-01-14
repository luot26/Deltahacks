function getInput() {
    onkeydown = (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            const input = document.getElementById("myInput").value;
            fetch("/submit", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ input })
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server
                console.log(data);
            
            })
            .catch(error => {
                // Handle any errors
                console.error(error);
            });
            
        }
    };
}
export default getInput;
