Foram identificadas 3 falhas no QuickJS, mecanismo JavaScript utilizado pelo Telegram Desktop.

1. Use-after-return (RCE): uma falha no gerenciamento de memória permite acessar referências inválidas, possibilitando executar programas no Windows. Foi demonstrado abrindo a Calculadora.

2. Use-after-free (RCE): uma falha no gerenciamento de memória de geradores permite acessar objetos já liberados, possibilitando execução de código. Também foi demonstrada abrindo a Calculadora.

3. Heap Underwrite (corrupção de memória): uma falha no tratamento de falta de memória provoca uma escrita de 16 bytes fora dos limites do heap, podendo causar corrupção de memória e travamento.
Impacto
- 2 falhas críticas: execução remota de código (RCE).
- 1 falha: corrupção de memória e possível negação de serviço (DoS).
- As duas primeiras foram testadas no Telegram Desktop 7.4.2 original, sem modificações.
Conclusão: as falhas demonstram que widgets maliciosos podem explorar problemas internos do QuickJS e comprometer a segurança do Telegram Desktop. A terceira falha ainda não demonstrou execução de código.

Posso também transformar esse resumo em um relatório técnico curto, no estilo de divulgação de vulnerabilidade (Security Advisory).
