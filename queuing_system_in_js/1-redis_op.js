import { print, createClient } from 'redis';

const client = createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});

async function setNewSchool(schoolName, value) {
    await client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
    const value = await client.get(schoolName);
    console.log(value);
}

client.connect().then(() => {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
    client.quit();
});
