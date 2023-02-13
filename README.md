<ol><li><p>Install Docker and Docker Compose:</p><ul><li><a href="https://docs.docker.com/get-docker/" target="_new">Docker Installation Guide</a></li><li><a href="https://docs.docker.com/compose/install/" target="_new">Docker Compose Installation Guide</a></li></ul></li><li><p>Clone the project repository:</p><code>git clone https://github.com/II9tka/proxy.git</code>
</li><li><p>Change into the project directory:</p><code>cd proxy
</code></li><li><p>Copy <code>env.example.prod</code> in <code>.env</code>:</p><code>cp env.example.prod .env
</code></li><li><p>Run project:</p><code>docker-compose -f docker-compose.prod.yml up --build
</code></li></ol>
