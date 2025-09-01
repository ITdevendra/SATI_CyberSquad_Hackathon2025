// src/dashboard/components/ClusterGraph.jsx
import React from "react";
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

const ClusterGraph = () => {
  // Sample cluster data (x, y = dimensions reduced via PCA/TSNE for visualization)
  const data = [
    { x: 10, y: 30, cluster: "Cluster A" },
    { x: 15, y: 35, cluster: "Cluster A" },
    { x: 30, y: 20, cluster: "Cluster B" },
    { x: 32, y: 22, cluster: "Cluster B" },
    { x: 50, y: 60, cluster: "Cluster C" },
    { x: 55, y: 65, cluster: "Cluster C" }
  ];

  return (
    <div className="chart-card">
      <h3>🧩 Cluster Graph</h3>
      <ResponsiveContainer width="100%" height={300}>
        <ScatterChart>
          <CartesianGrid />
          <XAxis type="number" dataKey="x" name="X" />
          <YAxis type="number" dataKey="y" name="Y" />
          <Tooltip cursor={{ strokeDasharray: "3 3" }} />
          <Scatter name="Clusters" data={data} fill="#82ca9d" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ClusterGraph;
