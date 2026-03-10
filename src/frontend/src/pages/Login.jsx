import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

const Login = () => {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    const success = await login(formData.username, formData.password);
    if (success) {
      navigate('/recipes');
    } else {
      setError('Usuario o contraseña incorrectos');
    }
    setLoading(false);
  };

  const containerStyle = {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f3f4f6',
  };

  const cardStyle = {
    backgroundColor: 'white',
    padding: '32px',
    borderRadius: '8px',
    boxShadow: '0 10px 15px rgba(0, 0, 0, 0.1)',
    width: '100%',
    maxWidth: '428px',
  };

  const titleStyle = {
    fontSize: '24px',
    fontWeight: 'bold',
    marginBottom: '24px',
    textAlign: 'center',
  };

  const errorStyle = {
    backgroundColor: '#fee2e2',
    border: '1px solid #fca5a5',
    color: '#b91c1c',
    padding: '12px 16px',
    marginBottom: '16px',
    borderRadius: '4px',
  };

  const formGroupStyle = {
    marginBottom: '16px',
  };

  const labelStyle = {
    display: 'block',
    color: '#374151',
    fontWeight: 'bold',
    marginBottom: '8px',
  };

  const inputStyle = {
    width: '100%',
    padding: '12px',
    border: '1px solid #d1d5db',
    borderRadius: '8px',
    fontSize: '16px',
    transition: 'border-color 0.2s',
  };

  const buttonStyle = {
    width: '100%',
    backgroundColor: '#f97316',
    color: 'white',
    padding: '12px',
    borderRadius: '8px',
    fontWeight: 'bold',
    border: 'none',
    cursor: 'pointer',
    transition: 'background-color 0.2s',
    opacity: loading ? 0.6 : 1,
  };

  const footerStyle = {
    marginTop: '16px',
    textAlign: 'center',
    color: '#6b7280',
  };

  const linkStyle = {
    color: '#f97316',
    textDecoration: 'none',
    cursor: 'pointer',
  };

  return (
    <div style={containerStyle}>
      <div style={cardStyle}>
        <h1 style={titleStyle}>Iniciar Sesión</h1>

        {error && <div style={errorStyle}>{error}</div>}

        <form onSubmit={handleSubmit}>
          <div style={formGroupStyle}>
            <label style={labelStyle}>Usuario</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              style={inputStyle}
              required
            />
          </div>

          <div style={formGroupStyle}>
            <label style={labelStyle}>Contraseña</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              style={inputStyle}
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            style={buttonStyle}
            onMouseOver={(e) => !loading && (e.target.style.backgroundColor = '#ea580c')}
            onMouseOut={(e) => !loading && (e.target.style.backgroundColor = '#f97316')}
          >
            {loading ? 'Cargando...' : 'Iniciar Sesión'}
          </button>
        </form>

        <p style={footerStyle}>
          ¿No tienes cuenta? <Link to="/register" style={linkStyle}>Regístrate</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
