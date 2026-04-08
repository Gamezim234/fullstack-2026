const { Client, LocalAuth, AuthStrategy } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client({
    AuthStrategy: new LocalAuth()
});

client.on('qr', (qr) => {
    qrcode.generate(qr, {small: true})
});

client.once('ready', () => {
    console.log('Bot está pronto!')
});
const userState = {};
const 

client.on('message', async(msg) =>{
    const chatd = msg.from;
    const body = msg.body.trim().toLocaleLowerCase();

    if (body == 'menu') {

    }
})

client.initialize()