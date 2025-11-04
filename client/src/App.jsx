import { useEffect, useState } from "react";

export default function App() {
  const [menu, setMenu] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/categories/with-items")
      .then((res) => res.json())
      .then((data) => setMenu(data))
      .catch((err) => console.error("Error fetching menu:", err));
  }, []);

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", padding: 24 }}>
      <h1>☕ Coffee Shop Menu</h1>

      {menu.length === 0 && <p>Loading menu...</p>}

      {menu.map((cat) => (
        <section key={cat.id} style={{ marginTop: 24 }}>
          <h2>{cat.name}</h2>
          <ul style={{ listStyle: "none", padding: 0 }}>
            {cat.items.map((item) => (
              <li
                key={item.id}
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  padding: "8px 0",
                  borderBottom: "1px solid #eee",
                }}
              >
                <div>
                  <strong>{item.name}</strong>
                  <p style={{ margin: "4px 0", color: "#555" }}>
                    {item.description}
                  </p>
                </div>
                <span>${item.price?.toFixed(2)}</span>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
