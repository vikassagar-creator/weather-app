const btn = document.getElementById("theme-btn");

const savedTheme = localStorage.getItem("theme") || "light";
document.documentElement.setAttribute("data-theme", savedTheme);

if (btn) {
    updateButton();

    btn.addEventListener("click", () => {
        const current = document.documentElement.getAttribute("data-theme");
        const next = current === "dark" ? "light" : "dark";

        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem("theme", next);

        updateButton();
    });
}

function updateButton() {
    if (!btn) return;

    const theme = document.documentElement.getAttribute("data-theme");

    btn.textContent = theme === "dark" ? "☀️" : "🌙";
}
