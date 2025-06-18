create database biblioteca;
    create table biblioteca.livros(
        --id integer primary key auto_increment
        id integer serial primary key,
        nome text not null,
        genero text not null
        auroes text not null
        );
insert into livros
    (nome, genero, autores) values
    ('Dom Casmurro', 'Romance', 'Machado de Assis')
--select * from 'livros'; (selecionar tudo de livros)
--select * from 'livros' where id=3; (selecionar tudo de id 3)


