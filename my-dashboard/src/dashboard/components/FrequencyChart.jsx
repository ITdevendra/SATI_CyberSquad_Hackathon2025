import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const FrequencyChart = ({ posts }) => {
  // Group posts by hour
  const freq = {};
  posts.forEach((p) => {
    const timestamp = p.createdAt || p.CreatedAt; // ✅ handle both
    if (timestamp) {
      const hour = new Date(timestamp).getHours();
      freq[hour] = (freq[hour] || 0) + 1;
    }
  });

  // Format into chart data
  const data = Array.from({ length: 24 }, (_, h) => ({
    hour: `${h}:00`,
    count: freq[h] || 0,
  }));

  return (
    <div className="card">
      <h2>⏱️ Posting Frequency</h2>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="hour" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Line type="monotone" dataKey="count" stroke="#FF8042" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default FrequencyChart;
