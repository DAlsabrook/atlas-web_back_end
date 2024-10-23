import { createClient } from 'redis';
import { promisify } from 'util';

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
    // this is working to create a promise out of the callback
    client.get = promisify(client.get);

    // This never resolves for some reason.
    client.get(schoolName).then((value) => {
        console.log(value);
    });
}

async function main() {
    await client.connect();

    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');

    await client.quit();
}

main().catch(console.error);
