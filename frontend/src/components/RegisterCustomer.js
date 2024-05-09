import { useState } from 'react';
import axios from 'axios';

function RegisterCustomer() {
  const [customer, setCustomer] = useState({
    name: '',
    dob: '',
    email: '',
    aadhar_number: '',
    assigned_mobile_number: '',
    current_plan_id: '',
  });

  const handleChange = (e) => {
    setCustomer({ ...customer, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://localhost:5000/customers', customer)
      .then((response) => {
        console.log('Customer registered:', response.data);
      })
      .catch((error) => {
        console.error('Error registering customer:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={customer.name}
        onChange={handleChange}
      />
      <input
        type="date"
        name="dob"
        placeholder="Date of Birth"
        value={customer.dob}
        onChange={handleChange}
      />
      <input
        type="email"
        name="email"
        placeholder="Email"
        value={customer.email}
        onChange={handleChange}
      />
      <input
        type="text"
        name="aadhar_number"
        placeholder="Aadhar Number"
        value={customer.aadhar_number}
        onChange={handleChange}
      />
      <input
        type="text"
        name="assigned_mobile_number"
        placeholder="Assigned Mobile Number"
        value={customer.assigned_mobile_number}
        onChange={handleChange}
      />
      <button type="submit">Register Customer</button>
    </form>
  );
}

export default RegisterCustomer;
