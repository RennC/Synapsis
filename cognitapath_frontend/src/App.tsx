import { Box, Typography } from "@mui/material";

function App() {
  return (
    <Box 
      sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center', 
        justifyContent: 'center', 
        height: '100vh' 
      }}
    >
      <Typography variant="h2" component="h1" gutterBottom>
        Bem-vindo ao CognitaPath
      </Typography>
      <Typography variant="h5">
        Seu assistente inteligente de aprendizado.
      </Typography>
      <Typography sx={{ mt: 2 }}>
        O código-fonte foi gerado. O próximo passo é configurar e rodar o projeto.
      </Typography>
    </Box>
  );
}

export default App;
