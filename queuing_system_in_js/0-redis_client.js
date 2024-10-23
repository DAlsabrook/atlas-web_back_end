import { createClient } from 'redis';

async function main() {
    const client = createClient();

    // Handle connection events
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    });

    client.on('error', (err) => {
        console.error('Redis client not connected to the server: ', err);
    });

    // await client.connect();

    // const value = await client.get('Holberton');
    // console.log('Value:', value);

    // await client.quit();
}

main().catch(console.error);
