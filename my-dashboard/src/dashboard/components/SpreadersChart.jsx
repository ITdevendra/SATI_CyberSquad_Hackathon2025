import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

const SpreadersChart = ({ data }) => {
  const formatted = Object.entries(data).map(([user, score]) => ({ user, score }));

  return (
    <div className="card">
      <h2>🚀 Top Spreaders</h2>
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={formatted}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="user" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="score" fill="#FF5733" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default SpreadersChart;
