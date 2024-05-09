import { useEffect, useState } from 'react';
import axios from 'axios';

function CustomerTable() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    axios
      .get('http://localhost:5000/customers')
      .then((response) => {
        console.log(response.data)
        setCustomers(response.data);
      })
      .catch((error) => {
        console.error('Error fetching customers:', error);
      });
  }, []); // Runs only once when the component is mounted

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Assigned Mobile Number</th>
        </tr>
      </thead>
      <tbody>
        {customers.map((customer) => (
          <tr key={customer.customer_id}>
            <td>{customer.name}</td>
            <td>{customer.email}</td>
            <td>{customer.assigned_mobile_number}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default CustomerTable;
