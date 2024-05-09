import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>Telecom Customer Management System</h1>
      <nav>
        <ul>
          <li>
            <Link to="/register">Register Customer</Link>
          </li>
          <li>
            <Link to="/customers">Customer Table</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;
