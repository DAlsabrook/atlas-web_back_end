// Works when executed or echoed into
process.stdout.write('Welcome to Atlas School, what is your name?\n');
process.stdin.on('data', data => {
    data = data.toString().trim();
    process.stdout.write(`Your name is: ${data}\n`);
    process.stdout.write('This important software is now closing\n');
    process.exit();
});
