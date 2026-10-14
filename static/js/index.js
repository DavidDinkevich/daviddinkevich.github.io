const abstractToggles = [...document.querySelectorAll(".abstract-toggle")];

function setAbstractExpanded(button, expanded) {
  const panelId = button.getAttribute("aria-controls");
  const panel = document.getElementById(panelId);

  if (!panel) {
    throw new Error(`Missing abstract panel: ${panelId}`);
  }

  button.setAttribute("aria-expanded", String(expanded));
  panel.hidden = !expanded;
}

for (const button of abstractToggles) {
  button.addEventListener("click", () => {
    const shouldExpand = button.getAttribute("aria-expanded") !== "true";

    for (const otherButton of abstractToggles) {
      setAbstractExpanded(otherButton, otherButton === button && shouldExpand);
    }
  });
}
