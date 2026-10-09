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

const supportsHover = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (supportsHover && !prefersReducedMotion) {
  for (const card of document.querySelectorAll("[data-preview-card]")) {
    const image = card.querySelector(".publication-preview img");

    if (!image) {
      throw new Error("Publication card is missing its preview image.");
    }

    const staticSource = image.dataset.staticSrc;
    const animatedSource = image.dataset.animatedSrc;

    if (!staticSource || !animatedSource) {
      throw new Error("Publication preview requires static and animated sources.");
    }

    const showAnimatedPreview = () => {
      if (image.src !== new URL(animatedSource, window.location.href).href) {
        image.src = animatedSource;
      }
    };

    const showStaticPreview = () => {
      image.src = staticSource;
    };

    card.addEventListener("pointerenter", showAnimatedPreview);
    card.addEventListener("pointerleave", showStaticPreview);
    card.addEventListener("focusin", showAnimatedPreview);
    card.addEventListener("focusout", (event) => {
      if (!card.contains(event.relatedTarget)) {
        showStaticPreview();
      }
    });
  }
}
