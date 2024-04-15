import { useState , useEffect} from 'react'
import ContactList from './ContactList'
import ContactForm from './ContactForm'
import './App.css'

function App() {

  const [contacts, setContacts] = useState([])
  useEffect(() => {

    fetchContacts()
  }, [])
  const fetchContacts = async () => {
    const response = await fetch('http://127.0.0.1:5000/contacts')
    if (!response.ok) {
      throw new Error('Failed to fetch contacts');
    }
    const data = await response.json()
    console.log(data)
    setContacts(data.contacts)
    console.log(data.contacts)
  }
  return (
    <>
      <ContactList contacts={contacts} />
      <ContactForm/>
    </>
  )
}

export default App
