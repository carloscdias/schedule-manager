# schedule-manager

UERJ Schedule Manager

## uso

```
python3 sm.py matricula -m metodo -o obrigatorias -e excluidas
```
Obrigatrórias e excluídas são parâmetros opcionais e devem seguir o padrão separado por vírgula como no exemplo abaixo.
```
python3 sm.py matricula -m aleatorio -e "Equações Diferenciais II,Estágio Supervisionado"
```
Executa o programa com o método aleatório desconsiderando as disciplinas Equações Diferenciais II e Estágio Supervisionado.

## formato da saída "matricula-codAlgoritmo-data.csv"

```
m1-seg,m1-ter,m1-qua,m1-qui,m1-sex,m1-sab
m2-seg,m2-ter,m2-qua,m2-qui,m2-sex,m2-sab
m3-seg,m3-ter,m3-qua,m3-qui,m3-sex,m3-sab
m4-seg,m4-ter,m4-qua,m4-qui,m4-sex,m4-sab
m5-seg,m5-ter,m5-qua,m5-qui,m5-sex,m5-sab
m6-seg,m6-ter,m6-qua,m6-qui,m6-sex,m6-sab
t1-seg,t1-ter,t1-qua,t1-qui,t1-sex,t1-sab
t2-seg,t2-ter,t2-qua,t2-qui,t2-sex,t2-sab
t3-seg,t3-ter,t3-qua,t3-qui,t3-sex,t3-sab
t4-seg,t4-ter,t4-qua,t4-qui,t4-sex,t4-sab
t5-seg,t5-ter,t5-qua,t5-qui,t5-sex,t5-sab
t6-seg,t6-ter,t6-qua,t6-qui,t6-sex,t6-sab
n1-seg,n1-ter,n1-qua,n1-qui,n1-sex,n1-sab
n2-seg,n2-ter,n2-qua,n2-qui,n2-sex,n2-sab
n3-seg,n3-ter,n3-qua,n3-qui,n3-sex,n3-sab
n4-seg,n4-ter,n4-qua,n4-qui,n4-sex,n4-sab
n5-seg,n5-ter,n5-qua,n5-qui,n5-sex,n5-sab
n6-seg,n6-ter,n6-qua,n6-qui,n6-sex,n6-sab
```

Com o código da disciplina ocupando as posições adequadas de acordo com o horário.



Contributors: Carlos Cardoso, Jhonatan Gomes, Rafael Firmino e Vitor Marchena.
