import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import RegisterCustomer from './components/RegisterCustomer';
import CustomerTable from './components/CustomerTable';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<RegisterCustomer />} />
        <Route path="/customers" element={<CustomerTable />} />
      </Routes>
    </Router>
  );
}

export default App;