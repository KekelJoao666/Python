--select, insert, update, merge
create table Alunos(
    ID int primary key,
    Nome varchar(50),
    Curso varchar(50)
);

--

insert into alunos(Nome,Curso)
values('Maria','Engenharia')

--

update alunos set Curso='Matematica' 
where ID=0;

--//--

Create Table produtos( 
    ID int AUTO_INCREMENT primary key, 
    Produto varchar(100),
    Preco float,
    QTD_Produto int
);

--

    insert into produtos(Produto, Preco, QTD_Produto)
    values('Banana','500.00','1000'),
          ('Caviar','2000','100'),


CREATE TABLE Clientes(
    ID INT primary key,
    Nome varchar(30)
    Email varchar(50)
);

select 'Nome', 'Email' FROM Clientes 
--WHERE 

INSERT INTO Clientes(Nome, Email)
VALUES(ANA, anaclara@gmail.com)

 --

UPDATE Clientes set Email ='novoemail@gmail.com' where ID=102
