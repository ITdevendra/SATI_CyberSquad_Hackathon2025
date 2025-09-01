import React from "react";
import "./poststable.css";

const PostsTable = ({ posts }) => {
  return (
    <div className="card">
      <h2>📝 Recent Posts</h2>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Account</th>
              <th>Text</th>
              <th>Hashtags</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            {posts.map((p, i) => (
              <tr key={i}>
                <td>{p.username}</td>
                <td>{p.content}</td>
                <td>{p.hashtags.join(" ")}</td>
                <td>{new Date(p.createdAt).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default PostsTable;
