let form = document.querySelector("form");
let responseDiv = document.querySelector("#response");

form.addEventListener("submit", (e) => {
	e.preventDefault();

	let formData = new FormData();
	formData.append(
		"text",
		document.getElementById("text-form").value
	);

	formData.append(
		"algorithm-type",
		document.getElementById("algorithm-select").value.toString()
	);
	
	document.getElementById("response").textContent = 'Waiting for a response...';
	
	// Send Fetch request
	fetch("https://michael099.pythonanywhere.com/analyze", {
		method: "POST",
		body: formData,
	})
		.then(function (response) {
			if (!response.ok) {
				throw new Error(
					"API is temp down. Please try again later."
				);
			}
			return response.text();
		})
		.then(function (data) {
			// Handle successful response
			document.getElementById("response").textContent = data; // Append response to div#response
		})
		.catch(function (error) {
			// Handle error
			console.error("Error:", error);
		});
});
