import { createClient } from 'redis';

const client = createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});

async function setNewSchool(schoolName, value) {
    const setValue = await client.set(schoolName, value);
    console.log('Reply:', setValue); // lol redis.print doesn't work
}

async function displaySchoolValue(schoolName) {
    const getValue = await client.get(schoolName);
    console.log(getValue);
}

client.connect().then(() => {
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
    client.quit();
});
