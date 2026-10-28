import sqlite3

# Criação de um banco de dados temporário em memória para testes
def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    conn.commit()
    return conn

def login(conn, username_input, password_input):
    cursor = conn.cursor()
    
    # VULNERABILIDADE CLÁSSICA: Concatenação direta de strings na query SQL (SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username_input}' AND password = '{password_input}'"
    
    print(f"[DEBUG] Executando query: {query}")
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        print("Login bem-sucedido! Acesso concedido.")
    else:
        print("Falha no login. Credenciais inválidas.")

if __name__ == "__main__":
    conexao = init_db()
    print("--- Teste de Login Inseguro ---")
    u = input("Usuário: ")
    p = input("Senha: ")
    login(conexao, u, p)