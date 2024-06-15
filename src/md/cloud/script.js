// docs/js/render_dns.js

document.addEventListener("DOMContentLoaded", function() {
    function renderDnsTable(dnsData) {
        const table = document.createElement('table');
        table.classList.add('dns-table');

        // Create table header
        const headerRow = table.insertRow();
        const headerDomain = headerRow.insertCell();
        headerDomain.textContent = 'Domain';
        const headerRecordType = headerRow.insertCell();
        headerRecordType.textContent = 'Record Type';
        const headerRecordName = headerRow.insertCell();
        headerRecordName.textContent = 'Record Name';
        const headerRecordValue = headerRow.insertCell();
        headerRecordValue.textContent = 'Record Value';

        // Populate table rows with DNS data
        for (const domain in dnsData) {
            dnsData[domain].forEach(record => {
                const row = table.insertRow();
                const cellDomain = row.insertCell();
                cellDomain.textContent = domain;
                const cellRecordType = row.insertCell();
                cellRecordType.textContent = record.type;
                const cellRecordName = row.insertCell();
                cellRecordName.textContent = record.name;
                const cellRecordValue = row.insertCell();
                cellRecordValue.textContent = record.content;
            });
        }

        return table;
    }

    function fetchDnsDataAndRenderTable() {
        fetch('/api/dns')
            .then(response => response.json())
            .then(dnsData => {
                const tableContainer = document.getElementById('dns-table-container');
                if (tableContainer) {
                    tableContainer.innerHTML = ''; // Clear loading message
                    tableContainer.appendChild(renderDnsTable(dnsData));
                }
            })
            .catch(error => {
                console.error('Error fetching DNS data:', error);
                const tableContainer = document.getElementById('dns-table-container');
                if (tableContainer) {
                    tableContainer.textContent = 'Failed to load DNS records.';
                }
            });
    }

    fetchDnsDataAndRenderTable();
});
