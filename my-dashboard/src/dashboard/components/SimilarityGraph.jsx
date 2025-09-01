// src/dashboard/components/SimilarityGraph.jsx
import React from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";

const SimilarityGraph = () => {
  // Sample similarity data (post1 vs post2 similarity scores)
  const data = [
    { pair: "user006-user012", similarity: 0.82 },
    { pair: "user006-user022", similarity: 0.76 },
    { pair: "user012-user027", similarity: 0.68 },
    { pair: "user022-user031", similarity: 0.72 },
    { pair: "user027-user031", similarity: 0.65 }
  ];

  return (
    <div className="chart-card">
      <h3>🔗 Post Similarity Graph</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="pair" />
          <YAxis domain={[0, 1]} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="similarity" stroke="#8884d8" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default SimilarityGraph;
