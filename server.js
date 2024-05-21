import { fastify } from "fastify"

const server = fastify()

server.get('/', () =>{
    return 'Helo World'
})

server.listen({
    port: 7070,
})
