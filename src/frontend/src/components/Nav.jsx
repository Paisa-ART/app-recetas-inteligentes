import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

const Nav = () => {
  const { user, logout } = useAuth();

  const navStyle = {
    backgroundColor: '#f97316',
    color: 'white',
    padding: '16px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  };

  const containerStyle = {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '0 16px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  };

  const logoStyle = {
    fontSize: '24px',
    fontWeight: 'bold',
    textDecoration: 'none',
    color: 'white',
  };

  const linkStyle = {
    color: 'white',
    textDecoration: 'none',
    marginRight: '20px',
    cursor: 'pointer',
  };

  const linksContainerStyle = {
    display: 'flex',
    gap: '16px',
    alignItems: 'center',
  };

  const logoutButtonStyle = {
    backgroundColor: '#dc2626',
    color: 'white',
    padding: '8px 16px',
    borderRadius: '6px',
    border: 'none',
    cursor: 'pointer',
    fontWeight: 'bold',
    transition: 'background-color 0.2s',
  };

  return (
    <nav style={navStyle}>
      <div style={containerStyle}>
        <Link to="/" style={logoStyle}>
          🍲 App Recetas
        </Link>

        <div style={linksContainerStyle}>
          {user ? (
            <>
              <Link to="/recipes" style={linkStyle}>
                Recetas
              </Link>
              <Link to="/favorites" style={linkStyle}>
                Favoritas
              </Link>
              <Link to="/shopping-lists" style={linkStyle}>
                Mis Listas
              </Link>
              <span style={{ fontSize: '14px' }}>{user.username}</span>
              <button
                onClick={logout}
                style={logoutButtonStyle}
                onMouseOver={(e) => e.target.style.backgroundColor = '#b91c1c'}
                onMouseOut={(e) => e.target.style.backgroundColor = '#dc2626'}
              >
                Salir
              </button>
            </>
          ) : (
            <>
              <Link to="/login" style={linkStyle}>
                Iniciar Sesión
              </Link>
              <Link to="/register" style={linkStyle}>
                Registrarse
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Nav;
