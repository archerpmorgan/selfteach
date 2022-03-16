taskkill //PID $(netstat -ano | findstr :3001 | head -n 1 | awk -F ' ' '{print $5}') //F 
taskkill //PID $(netstat -ano | findstr :3000 | head -n 1 | awk -F ' ' '{print $5}') //F 
