import React from "react";
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#aa66cc"];

const AccountsChart = ({ data }) => {
  console.log(data);
  
  const formatted = data.map((username, post_count) => ({ acc: username, posts: post_count }));

  return (
    <div className="card">
      <h2>👤 Top Accounts</h2>
      <ResponsiveContainer width="100%" height={250}>
        <PieChart>
          <Pie
            data={formatted}
            dataKey="posts"
            nameKey="acc"
            outerRadius={90}
            label
          >
            {formatted.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AccountsChart;
