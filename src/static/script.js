window.fetchFromDrive = async function () {
    const driveUrl = document.getElementById("driveUrl").value.trim();
    const statusElement = document.getElementById("fetchStatus");
    const previewDiv = document.getElementById("preview");

    statusElement.textContent = "";
    previewDiv.innerHTML = "";

    if (!driveUrl) {
        statusElement.textContent = "Please enter a valid Google Drive link.";
        return;
    }

    try {
        statusElement.textContent = "Fetching file from Google Drive...";

        const response = await fetch(`/fetch_from_drive?file_url=${encodeURIComponent(driveUrl)}`, {
            method: "POST"
        });

        let result;
        try {
            // Try parsing as JSON
            result = await response.clone().json();
        } catch (jsonError) {
            // Use clone to preserve stream
            const errorText = await response.clone().text();
            throw new Error("Unexpected server response: " + errorText);
        }

        if (!response.ok) {
            throw new Error(result?.detail || "Fetch failed.");
        }

        statusElement.textContent = result.message;

        if (result.preview && result.preview.length > 0) {
            const headers = Object.keys(result.preview[0]);
            const table = document.createElement("table");

            const thead = document.createElement("thead");
            const headerRow = document.createElement("tr");
            headers.forEach(header => {
                const th = document.createElement("th");
                th.textContent = header;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);

            const tbody = document.createElement("tbody");
            result.preview.forEach(row => {
                const tr = document.createElement("tr");
                headers.forEach(header => {
                    const td = document.createElement("td");
                    td.textContent = row[header];
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);

            previewDiv.appendChild(table);
        } else {
            previewDiv.innerHTML = "<p>No preview data found.</p>";
        }

    } catch (error) {
        console.error("Fetch error:", error);
        statusElement.textContent = "❌ Error: " + error.message;
    }
};


async function submitQuery() {
    const queryInput = document.getElementById('queryInput');
    const queryStatus = document.getElementById('queryStatus');
    const responseDiv = document.getElementById('response');
    const query = queryInput.value.trim();

    if (!query) {
        queryStatus.textContent = 'Please enter a query.';
        return;
    }

    try {
        queryStatus.textContent = 'Processing...';
        const response = await fetch('/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        const result = await response.json();
        if (response.ok) {
            queryStatus.textContent = '';
            responseDiv.textContent = result.response;
        } else {
            queryStatus.textContent = result.detail || 'Query failed.';
        }
    } catch (error) {
        queryStatus.textContent = 'Error processing query.';
        console.error(error);
    }
}