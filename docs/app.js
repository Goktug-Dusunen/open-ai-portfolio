const state = { artifacts: [], kind: "all", owner: "all", query: "", visible: 18 };
const number = new Intl.NumberFormat("en", { notation: "compact", maximumFractionDigits: 1 });

function flattenCatalog(catalog) {
  return Object.entries(catalog.owners).flatMap(([owner, kinds]) =>
    Object.entries(kinds).flatMap(([kind, artifacts]) =>
      artifacts.map((artifact) => ({ ...artifact, owner, kind }))
    )
  );
}

function setMetrics(catalog) {
  const totals = { models: 0, datasets: 0, spaces: 0, downloads: 0 };
  Object.values(catalog.owners).forEach((kinds) => {
    Object.entries(kinds).forEach(([kind, artifacts]) => {
      totals[kind] += artifacts.length;
      totals.downloads += artifacts.reduce((sum, item) => sum + item.downloads, 0);
    });
  });
  Object.entries(totals).forEach(([key, value]) => {
    document.querySelector(`[data-metric="${key}"]`).textContent = number.format(value);
  });
  const updated = new Date(catalog.generated_at);
  document.querySelector("#sync-status").textContent = `Verified from public Hugging Face APIs · ${updated.toLocaleDateString("en", { year: "numeric", month: "short", day: "numeric" })}`;
}

function artifactCard(item) {
  const link = document.createElement("a");
  link.className = "artifact";
  link.href = item.url;
  link.target = "_blank";
  link.rel = "noreferrer";

  const top = document.createElement("div");
  top.className = "artifact-top";
  const kind = document.createElement("span");
  kind.className = "artifact-kind";
  kind.textContent = item.kind.slice(0, -1);
  const owner = document.createElement("span");
  owner.className = "artifact-owner";
  owner.textContent = item.owner;
  top.append(kind, owner);

  const title = document.createElement("h3");
  title.textContent = item.id.split("/").pop();
  const task = document.createElement("p");
  task.textContent = item.task || (item.kind === "spaces" ? "Interactive demo" : item.kind === "datasets" ? "Public dataset" : "Model");
  const meta = document.createElement("div");
  meta.className = "artifact-meta";
  meta.textContent = `${number.format(item.downloads)} downloads · ${item.likes} likes`;
  link.append(top, title, task, meta);
  return link;
}

function filteredArtifacts() {
  return state.artifacts
    .filter((item) => state.kind === "all" || item.kind === state.kind)
    .filter((item) => state.owner === "all" || item.owner === state.owner)
    .filter((item) => `${item.id} ${item.task || ""}`.toLowerCase().includes(state.query))
    .sort((a, b) => b.downloads - a.downloads || b.likes - a.likes || a.id.localeCompare(b.id));
}

function render() {
  const items = filteredArtifacts();
  const grid = document.querySelector("#catalog-grid");
  grid.replaceChildren(...items.slice(0, state.visible).map(artifactCard));
  document.querySelector("#result-count").textContent = `${items.length} public artifacts`;
  document.querySelector("#load-more").hidden = state.visible >= items.length;
}

document.querySelectorAll("[data-kind]").forEach((button) => button.addEventListener("click", () => {
  document.querySelectorAll("[data-kind]").forEach((item) => item.classList.remove("active"));
  button.classList.add("active");
  state.kind = button.dataset.kind;
  state.visible = 18;
  render();
}));

document.querySelectorAll("[data-owner]").forEach((button) => button.addEventListener("click", () => {
  const wasActive = button.classList.contains("active");
  document.querySelectorAll("[data-owner]").forEach((item) => item.classList.remove("active"));
  state.owner = wasActive ? "all" : button.dataset.owner;
  button.classList.toggle("active", !wasActive);
  state.visible = 18;
  render();
}));

document.querySelector("#search").addEventListener("input", (event) => {
  state.query = event.target.value.trim().toLowerCase();
  state.visible = 18;
  render();
});
document.querySelector("#load-more").addEventListener("click", () => { state.visible += 18; render(); });

fetch("portfolio.json")
  .then((response) => { if (!response.ok) throw new Error(`HTTP ${response.status}`); return response.json(); })
  .then((catalog) => { state.artifacts = flattenCatalog(catalog); setMetrics(catalog); render(); })
  .catch(() => { document.querySelector("#sync-status").textContent = "Catalog unavailable. Visit Hugging Face for the current portfolio."; });
