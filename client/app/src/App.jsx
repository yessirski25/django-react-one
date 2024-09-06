import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([]);
  const [contactName, setContactName] = useState("");
  const [contactNumber, setContactNumber] = useState(0);

  const [newName, setNewName] = useState("");

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    try{
      const response = await fetch("http://127.0.0.1:8000/api/contacts/");
      const data = await response.json();
      setContacts(data);
    } catch(err) {
      console.log(err);
    }
  }

  const addContact = async () => {
    const contactData = {
      contactName,
      contactNumber
    };
    try {
      const response = await fetch("http://127.0.0.1:8000/api/contacts/create/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(contactData),
      });

      const data = await response.json()
      setContacts((prev) => [...prev, data]);
    } catch (err) {
      console.log(err);
    }
  };

  const updateName = async (pk, contactNumber) => {
    const contactData = {
      contactName: newName,
      contactNumber
    };
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/contacts/${pk}/update/`, {
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(contactData),
      });

      const data = await response.json()
      setContacts((prev) => prev.map((contact) => {
        if (contact.id === pk) {
          return data;
        } else {
          return contact;
        }
      }));
    } catch (err) {
      console.log(err);
    }
  };

  const deleteContact = async (pk) => {
    const contactData = {
      contactName: newName,
      contactNumber
    };
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/contacts/${pk}/delete/`, {
        method: "DELETE",
      });

      setContacts((prev) => prev.filter((book) => book.id !== pk))
    } catch (err) {
      console.log(err);
    }
  }

  return (
    <>
      <h1> Phone Book / Contacts </h1>

      <div class='addContact'>
        <input type="text" placeholder='Contact Name...' onChange={(e) => setContactName(e.target.value)}/>
        <input type="tel" placeholder='Phone Number...' onChange={(e) => setContactNumber(e.target.value)}/>
        <button onClick={addContact}>Add Contact</button>
      </div>
      {contacts.map((contact) => <div class="items">
        {" "}
        <p>Contact Name: {contact.contactName}</p>
        <p>Contact Number: {contact.contactNumber}</p>
        <input type='text' placeholder='New Name' onChange={(e) => setNewName(e.target.value)} />
        <button onClick={() => updateName(contact.id, contact.contactNumber)}>Edit Name</button>
        <button onClick={() => deleteContact(contact.id)}>
          Delete Contact
        </button>
      </div>)}
    </>
  )
}

export default App
