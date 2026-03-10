import React from 'react';
import { useAuth } from '../hooks/useAuth';
import { Link } from 'react-router-dom';

const Home = () => {
  const { user } = useAuth();

  const containerStyle = {
    minHeight: '100vh',
    backgroundImage: 'linear-gradient(to bottom, #fed7aa, white)',
  };

  const contentStyle = {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '48px 16px',
  };

  const titleStyle = {
    fontSize: '48px',
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: '16px',
  };

  const subtitleStyle = {
    fontSize: '20px',
    textAlign: 'center',
    color: '#4b5563',
    marginBottom: '32px',
  };

  const gridStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '32px',
    marginBottom: '48px',
  };

  const cardStyle = {
    backgroundColor: 'white',
    padding: '24px',
    borderRadius: '8px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
    transition: 'box-shadow 0.2s',
  };

  const cardTitleStyle = {
    fontSize: '20px',
    fontWeight: 'bold',
    marginBottom: '16px',
  };

  const cardTextStyle = {
    color: '#4b5563',
    marginBottom: '16px',
    lineHeight: '1.6',
  };

  const centerStyle = {
    textAlign: 'center',
  };

  const buttonContainerStyle = {
    display: 'flex',
    gap: '16px',
    justifyContent: 'center',
  };

  const buttonStyle = {
    padding: '12px 32px',
    borderRadius: '8px',
    fontWeight: 'bold',
    border: 'none',
    cursor: 'pointer',
    fontSize: '16px',
    textDecoration: 'none',
    display: 'inline-block',
    transition: 'background-color 0.2s',
  };

  const primaryButtonStyle = {
    ...buttonStyle,
    backgroundColor: '#f97316',
    color: 'white',
  };

  const secondaryButtonStyle = {
    ...buttonStyle,
    backgroundColor: '#10b981',
    color: 'white',
  };

  return (
    <div style={containerStyle}>
      <div style={contentStyle}>
        <h1 style={titleStyle}>🍲 App Recetas Inteligentes</h1>
        <p style={subtitleStyle}>Desarrollar Software es como Preparar unos Fríjoles</p>

        <div style={gridStyle}>
          <div style={cardStyle}>
            <div style={cardTitleStyle}>📖 Biblioteca de Recetas</div>
            <p style={cardTextStyle}>
              Accede a una amplia colección de recetas tradicionales, especialmente fríjoles. 
              Busca por nombre, ingrediente o tipo.
            </p>
          </div>

          <div style={cardStyle}>
            <div style={cardTitleStyle}>🧮 Ajuste Automático</div>
            <p style={cardTextStyle}>
              Cambia el número de personas y el sistema recalcularán automáticamente 
              todas las cantidades de ingredientes.
            </p>
          </div>

          <div style={cardStyle}>
            <div style={cardTitleStyle}>🛒 Lista de Compras</div>
            <p style={cardTextStyle}>
              Genera listas de compra en PDF listas para llevar al mercado, 
              con cantidades exactas y costos.
            </p>
          </div>

          <div style={cardStyle}>
            <div style={cardTitleStyle}>⏱️ Temporizador</div>
            <p style={cardTextStyle}>
              Controlador de tiempos con alertas para que no se queme nada. 
              Sigue cada paso sin estrés.
            </p>
          </div>

          <div style={cardStyle}>
            <div style={cardTitleStyle}>💵 Cálculo de Costos</div>
            <p style={cardTextStyle}>
              Muestra costo por ingrediente, total y por porción. 
              Ayuda a presupuestar tus comidas.
            </p>
          </div>

          <div style={cardStyle}>
            <div style={cardTitleStyle}>⭐ Recetas Favoritas</div>
            <p style={cardTextStyle}>
              Marca tus recetas favoritas y accede a ellas rápidamente. 
              Personaliza tu experiencia.
            </p>
          </div>
        </div>

        <div style={centerStyle}>
          {!user ? (
            <>
              <p style={{ marginBottom: '24px', fontSize: '18px', color: '#4b5563' }}>
                ¿Listo para comenzar? Inicia sesión o crea una cuenta
              </p>
              <div style={buttonContainerStyle}>
                <Link
                  to="/login"
                  style={primaryButtonStyle}
                  onMouseOver={(e) => e.target.style.backgroundColor = '#ea580c'}
                  onMouseOut={(e) => e.target.style.backgroundColor = '#f97316'}
                >
                  Iniciar Sesión
                </Link>
                <Link
                  to="/register"
                  style={secondaryButtonStyle}
                  onMouseOver={(e) => e.target.style.backgroundColor = '#059669'}
                  onMouseOut={(e) => e.target.style.backgroundColor = '#10b981'}
                >
                  Registrarse
                </Link>
              </div>
            </>
          ) : (
            <>
              <p style={{ marginBottom: '24px', fontSize: '18px', color: '#4b5563' }}>
                ¡Bienvenido, {user.first_name || user.username}!
              </p>
              <Link
                to="/recipes"
                style={primaryButtonStyle}
                onMouseOver={(e) => e.target.style.backgroundColor = '#ea580c'}
                onMouseOut={(e) => e.target.style.backgroundColor = '#f97316'}
              >
                Ver Recetas
              </Link>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
