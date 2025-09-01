import { useEffect, useState } from "react";
import "./dashboard.css";

import PostsTable from "./components/PostsTable";
import HashtagChart from "./components/TopHashtags";
import AccountsChart from "./components/AccountsChart";
import SimilarityGraph from "./components/SimilarityGraph";
import ClusterGraph from "./components/ClusterGraph";
import FrequencyChart from "./components/FrequencyChart";
import SpreadersChart from "./components/SpreadersChart";

const Dashboard = () => {
  const [query, setQuery] = useState("khalistan"); // default search
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  // function to fetch data
  const fetchData = (searchQuery) => {
    setLoading(true);
    fetch(`http://localhost:8000/detect?query=${encodeURIComponent(searchQuery)}`)
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("API Error:", err))
      .finally(() => setLoading(false));
  };

  // fetch default query on first load
  useEffect(() => {
    fetchData(query);
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim() !== "") {
      fetchData(query);
    }
  };

  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">📊 Campaign Detection Dashboard</h1>

      {/* 🔎 Search Bar */}
      <form onSubmit={handleSearch} className="search-bar">
        <input
          type="text"
          placeholder="Enter query (e.g. khalistan)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>

      {loading && <h2>Loading...</h2>}

      {!loading && data && (
        <>
          <div className="dashboard-section">
            <PostsTable posts={data.retrievedPosts} />
          </div>

          <div className="dashboard-grid">
            <HashtagChart data={data.topHashtags} />
            <AccountsChart data={data.topAccounts} />
          </div>

          <div className="dashboard-grid">
            <FrequencyChart posts={data.retrievedPosts} />
            <SpreadersChart data={data.topSpreaders} />
          </div>

          <div className="dashboard-grid">
            <SimilarityGraph data={data.similarPosts} />
            <ClusterGraph data={data.graphClusters} />
          </div>
        </>
      )}
    </div>
  );
};

export default Dashboard;
