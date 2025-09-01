import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const HashtagChart = ({ data }) => {
  if (!data || data.length === 0) {
    return <p>No hashtags available</p>;
  }

  const formatted = data.map(([tag, count]) => ({ tag, count }));

  return (
    <div className="bg-white p-4 rounded-2xl shadow">
      <h3 className="text-lg font-semibold mb-2">Top Hashtags</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={formatted}>
          <XAxis dataKey="tag" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#3b82f6" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default HashtagChart;
