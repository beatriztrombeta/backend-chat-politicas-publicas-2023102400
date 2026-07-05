SQL_QUERIES = {
    1: """
        SELECT
            COALESCE(NULLIF(TRIM(a.sexo), ''), 'Não informado') AS sexo,
            COUNT(*) AS total_alunos,
            ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
        FROM aluno a
        GROUP BY 1
        ORDER BY total_alunos DESC, sexo;
    """,
    2: """
        SELECT
            COALESCE(NULLIF(TRIM(a.raca_cor), ''), 'Não informado') AS raca_cor,
            COUNT(*) AS total_alunos,
            ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
        FROM aluno a
        GROUP BY 1
        ORDER BY total_alunos DESC, raca_cor;
    """,
    3: """
        SELECT
            cp.nome_campus,
            COUNT(*) AS total_alunos,
            ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
        FROM aluno a
        JOIN curso c       ON c.id_curso = a.id_curso
        JOIN unidade u     ON u.id_unidade = c.id_unidade
        JOIN campus cp     ON cp.id_campus = u.id_campus
        GROUP BY cp.nome_campus
        ORDER BY total_alunos DESC, cp.nome_campus;
    """,
    4: """
        SELECT
            c.nome_curso,
            COUNT(*) AS total_alunos,
            ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
        FROM aluno a
        JOIN curso c ON c.id_curso = a.id_curso
        GROUP BY c.nome_curso
        ORDER BY total_alunos DESC, c.nome_curso;
    """,
    5: """
SELECT
  ROUND(AVG(a.idade_matricula), 2) AS media_idade_matricula,
  MIN(a.idade_matricula) AS idade_minima,
  MAX(a.idade_matricula) AS idade_maxima,
  COUNT(a.idade_matricula) AS alunos_com_idade
FROM aluno a
WHERE a.idade_matricula IS NOT NULL;
    """,
    6: """
SELECT
  c.nome_curso,
  COUNT(a.idade_matricula) AS alunos_com_idade,
  ROUND(AVG(a.idade_matricula), 2) AS media_idade,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY a.idade_matricula) AS mediana_idade,
  MIN(a.idade_matricula) AS idade_minima,
  MAX(a.idade_matricula) AS idade_maxima
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
WHERE a.idade_matricula IS NOT NULL
GROUP BY c.nome_curso
ORDER BY media_idade DESC, c.nome_curso;
    """,
    7: """
SELECT
  COALESCE(NULLIF(TRIM(a.raca_cor), ''), 'Não informado') AS raca_cor,
  COUNT(*) AS total_alunos,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM aluno), 2) AS percentual
FROM aluno a
GROUP BY 1
ORDER BY percentual DESC, raca_cor;
    """,
    8: """
SELECT
  COALESCE(NULLIF(TRIM(a.pais_origem), ''), 'Não informado')   AS pais_origem,
  COALESCE(NULLIF(TRIM(a.estado_origem), ''), 'Não informado') AS estado_origem,
  COALESCE(NULLIF(TRIM(a.cidade_origem), ''), 'Não informado') AS cidade_origem,
  COUNT(*) AS total_alunos
FROM aluno a
GROUP BY 1, 2, 3
ORDER BY total_alunos DESC, pais_origem, estado_origem, cidade_origem;
    """,
    9: """
SELECT
  c.nome_curso,
  ROUND(AVG(a.avg_nota), 2) AS media_avg_nota,
  ROUND(AVG(a.cr), 2) AS media_cr,
  COUNT(*) AS total_alunos
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
GROUP BY c.nome_curso
ORDER BY media_avg_nota DESC NULLS LAST, media_cr DESC NULLS LAST, c.nome_curso;
    """,
    10: """
SELECT
  c.nome_curso,
  CASE
    WHEN a.avg_nota IS NULL THEN 'Sem nota'
    WHEN a.avg_nota >= 0 AND a.avg_nota < 2 THEN '0-2'
    WHEN a.avg_nota >= 2 AND a.avg_nota < 4 THEN '2-4'
    WHEN a.avg_nota >= 4 AND a.avg_nota < 6 THEN '4-6'
    WHEN a.avg_nota >= 6 AND a.avg_nota < 8 THEN '6-8'
    WHEN a.avg_nota >= 8 AND a.avg_nota <= 10 THEN '8-10'
    ELSE 'Fora da escala'
  END AS faixa_nota,
  COUNT(*) AS total_alunos
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
GROUP BY c.nome_curso, faixa_nota
ORDER BY c.nome_curso, faixa_nota;
    """,
    11: """
SELECT
  ROUND(AVG(a.cr), 2) AS media_cr,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY a.cr) AS mediana_cr,
  MIN(a.cr) AS cr_minimo,
  MAX(a.cr) AS cr_maximo,
  COUNT(a.cr) AS alunos_com_cr
FROM aluno a
WHERE a.cr IS NOT NULL;
    """,
    12: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  ROUND(AVG(a.avg_nota), 2) AS media_avg_nota,
  ROUND(AVG(a.cr), 2) AS media_cr,
  ROUND(AVG(a.perc_reprovacao), 2) AS media_perc_reprovacao,
  ROUND(AVG(a.perc_exames), 2) AS media_perc_exames
FROM aluno a
GROUP BY 1
ORDER BY 1;
    """,
    13: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existe campo/tabela de nota ENEM em 01init.sql' AS detalhe;
    """,
    14: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Sem coluna de nota ENEM não é possível calcular correlação com CR' AS detalhe;
    """,
    15: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não usa cotas'
    ELSE 'Usa cotas / ação afirmativa registrada em COTAS'
  END AS grupo,
  COUNT(*) AS total_alunos,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
FROM aluno a
GROUP BY 1
ORDER BY total_alunos DESC;
    """,
    16: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existe tabela/campos de questionário socioeconômico em 01init.sql' AS detalhe;
    """,
    17: """
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existe coluna de escolaridade dos pais no schema atual' AS detalhe;
    """,
    18: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existe coluna de renda familiar no schema atual' AS detalhe;
    """,
    19: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existe coluna de moradia no schema atual' AS detalhe;
    """,
    20: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Sem nota ENEM não há comparação entre cotistas e não cotistas' AS detalhe;
    """,
    21: """
SELECT
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(
    100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*),
    2
  ) AS taxa_evasao_percentual
FROM aluno a;
    """,
    22: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(
    100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*),
    2
  ) AS taxa_evasao_percentual
FROM aluno a
GROUP BY 1
ORDER BY 1;
    """,
    23: """
SELECT
  c.nome_curso,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) AS total_trancamento,
  ROUND(
    100.0 * SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) / COUNT(*),
    2
  ) AS taxa_trancamento_percentual
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
GROUP BY c.nome_curso
ORDER BY taxa_trancamento_percentual DESC, c.nome_curso;
    """,
    24: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) AS total_trancamento,
  ROUND(
    100.0 * SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) / COUNT(*),
    2
  ) AS taxa_trancamento_percentual
FROM aluno a
GROUP BY 1
ORDER BY 1;
    """,
    25: """
SELECT
  ROUND(AVG(a.data_desvinculo::date - MAKE_DATE(a.ano_matricula, 1, 1)), 2) AS media_dias_ate_desvinculo,
  MIN(a.data_desvinculo::date - MAKE_DATE(a.ano_matricula, 1, 1)) AS min_dias,
  MAX(a.data_desvinculo::date - MAKE_DATE(a.ano_matricula, 1, 1)) AS max_dias,
  COUNT(*) AS alunos_considerados
FROM aluno a
WHERE a.data_desvinculo IS NOT NULL
  AND a.ano_matricula IS NOT NULL
  AND a.situacao NOT IN ('MATRICULADO', 'CONCLUIDO');
    """,
    26: """
SELECT
  COALESCE(NULLIF(TRIM(a.motivo_desvinculo), ''), 'Não informado') AS motivo_desvinculo,
  COUNT(*) AS total_alunos,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
FROM aluno a
WHERE a.situacao NOT IN ('MATRICULADO', 'CONCLUIDO')
GROUP BY 1
ORDER BY total_alunos DESC, motivo_desvinculo;
    """,
    27: """
SELECT
  COALESCE(NULLIF(TRIM(c.modalidade), ''), 'Não informada') AS modalidade,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) AS total_trancamento,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual,
  ROUND(100.0 * SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS taxa_trancamento_percentual
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
GROUP BY 1
ORDER BY taxa_evasao_percentual DESC, taxa_trancamento_percentual DESC, modalidade;
    """,
    28: """
SELECT
  CORR(a.cr, CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0.0 ELSE 1.0 END) AS correlacao_cr_evasao,
  CORR(a.cr, CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1.0 ELSE 0.0 END) AS correlacao_cr_trancamento
FROM aluno a
WHERE a.cr IS NOT NULL;
    """,
    29: """
SELECT
  p.periodo,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual
FROM aluno a
JOIN curso c   ON c.id_curso = a.id_curso
JOIN periodo p ON p.id_periodo = c.id_periodo
GROUP BY p.periodo
ORDER BY taxa_evasao_percentual DESC, p.periodo;
    """,
    30: """
SELECT
  COALESCE(NULLIF(TRIM(a.tipo_ingresso), ''), 'Não informado') AS tipo_ingresso,
  COUNT(*) AS total_alunos,
  ROUND(AVG(a.avg_nota), 2) AS media_avg_nota,
  ROUND(AVG(a.cr), 2) AS media_cr,
  ROUND(AVG(a.perc_reprovacao), 2) AS media_perc_reprovacao
FROM aluno a
GROUP BY 1
ORDER BY media_avg_nota DESC NULLS LAST, media_cr DESC NULLS LAST, tipo_ingresso;
    """,
    31: """
SELECT
  COALESCE(NULLIF(TRIM(a.tipo_ingresso), ''), 'Não informado') AS tipo_ingresso,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual
FROM aluno a
GROUP BY 1
ORDER BY taxa_evasao_percentual DESC, tipo_ingresso;
    """,
    32: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'ALUNO_DISCIPLINA não possui semestre/período da disciplina cursada pelo aluno' AS detalhe;
    """,
    33: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  ROUND(AVG(a.cr), 2) AS media_cr,
  ROUND(STDDEV_POP(a.cr), 2) AS desvio_padrao_cr,
  ROUND(AVG(a.avg_nota), 2) AS media_avg_nota,
  ROUND(STDDEV_POP(a.avg_nota), 2) AS desvio_padrao_avg_nota
FROM aluno a
GROUP BY 1
ORDER BY 1;
    """,
    34: """
SELECT
  COUNT(*) AS alunos_com_pelo_menos_um_ano,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 1 ELSE 0 END) AS retidos_ou_concluidos,
  ROUND(
    100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 1 ELSE 0 END) / COUNT(*),
    2
  ) AS taxa_retencao_apos_primeiro_ano
FROM aluno a
WHERE a.ano_matricula IS NOT NULL
  AND a.ano_matricula <= EXTRACT(YEAR FROM CURRENT_DATE) - 1;
    """,
    35: """
SELECT
  a.ano_matricula,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual
FROM aluno a
WHERE a.ano_matricula IS NOT NULL
GROUP BY a.ano_matricula
ORDER BY a.ano_matricula;
    """,
    36: """
SELECT
  EXTRACT(MONTH FROM a.data_desvinculo) AS mes,
  COUNT(*) AS total_desvinculos,
  SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) AS total_trancamentos,
  SUM(CASE WHEN a.situacao NOT IN ('MATRICULADO', 'CONCLUIDO') THEN 1 ELSE 0 END) AS total_evasoes,
  ROUND(100.0 * SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS perc_trancamentos_no_mes,
  ROUND(100.0 * SUM(CASE WHEN a.situacao NOT IN ('MATRICULADO', 'CONCLUIDO') THEN 1 ELSE 0 END) / COUNT(*), 2) AS perc_evasoes_no_mes
FROM aluno a
WHERE a.data_desvinculo IS NOT NULL
GROUP BY 1
ORDER BY 1;
    """,
    37: """
SELECT
  a.ano_matricula,
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY a.ano_matricula), 2) AS percentual_no_ano
FROM aluno a
WHERE a.ano_matricula IS NOT NULL
GROUP BY a.ano_matricula, grupo_cotas
ORDER BY a.ano_matricula, grupo_cotas;
    """,
    38: """
SELECT
  a.ano_matricula,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 0 ELSE 1 END) AS total_cotistas,
  ROUND(
    100.0 * SUM(CASE WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 0 ELSE 1 END) / COUNT(*),
    2
  ) AS percentual_cotistas,
  ROUND(AVG(CASE WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN NULL ELSE a.cr END), 2) AS media_cr_cotistas,
  ROUND(AVG(CASE WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN NULL ELSE a.avg_nota END), 2) AS media_nota_cotistas
FROM aluno a
WHERE a.ano_matricula IS NOT NULL
GROUP BY a.ano_matricula
ORDER BY a.ano_matricula;
    """,
    39: """
SELECT
  c.nome_curso,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
GROUP BY c.nome_curso
ORDER BY taxa_evasao_percentual DESC, c.nome_curso;
    """,
    40: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) AS total_trancamento,
  ROUND(100.0 * SUM(CASE WHEN UPPER(COALESCE(a.situacao, '')) LIKE '%TRANC%' THEN 1 ELSE 0 END) / COUNT(*), 2) AS taxa_trancamento_percentual
FROM aluno a
GROUP BY 1
ORDER BY taxa_trancamento_percentual DESC;

    """,
    41: """
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existe coluna de renda/baixa renda no schema atual' AS detalhe;
    """,
    42: """
SELECT
  COALESCE(NULLIF(TRIM(c.modalidade), ''), 'Não informada') AS modalidade,
  COUNT(*) AS total_cotistas,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS cotistas_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_cotistas_percentual
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
WHERE COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') NOT IN ('NAO', 'NÃO', 'N', '0')
GROUP BY 1
ORDER BY taxa_evasao_cotistas_percentual DESC, modalidade;
    """,
    43: """
SELECT
  COALESCE(NULLIF(TRIM(a.estado_origem), ''), 'Não informado') AS estado_origem,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual
FROM aluno a
GROUP BY 1
HAVING COUNT(*) >= 5
ORDER BY taxa_evasao_percentual DESC, total_alunos DESC, estado_origem;
    """,
    44: """
SELECT
  COALESCE(NULLIF(TRIM(a.pais_origem), ''), 'Não informado')   AS pais_origem,
  COALESCE(NULLIF(TRIM(a.estado_origem), ''), 'Não informado') AS estado_origem,
  COALESCE(NULLIF(TRIM(a.cidade_origem), ''), 'Não informado') AS cidade_origem,
  COUNT(*) AS total_alunos
FROM aluno a
WHERE a.situacao NOT IN ('MATRICULADO', 'CONCLUIDO')
GROUP BY 1, 2, 3
ORDER BY total_alunos DESC, pais_origem, estado_origem, cidade_origem;
    """,
    45: """
SELECT
  COALESCE(NULLIF(TRIM(a.estado_origem), ''), 'Não informado') AS estado_origem,
  COUNT(*) AS total_alunos,
  ROUND(AVG(a.cr), 2) AS media_cr,
  ROUND(AVG(a.avg_nota), 2) AS media_avg_nota
FROM aluno a
GROUP BY 1
HAVING COUNT(*) >= 5
ORDER BY media_cr DESC NULLS LAST, media_avg_nota DESC NULLS LAST, estado_origem;
    """,
    46: """
SELECT
  COALESCE(NULLIF(TRIM(a.raca_cor), ''), 'Não informado') AS raca_cor,
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  ROUND(AVG(a.cr), 2) AS media_cr,
  ROUND(AVG(a.avg_nota), 2) AS media_avg_nota
FROM aluno a
GROUP BY 1, 2
ORDER BY raca_cor, grupo_cotas;
    """,
    47: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Não cotista'
    ELSE 'Cotista'
  END AS grupo_cotas,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 1 ELSE 0 END) AS total_retidos_ou_concluidos,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 1 ELSE 0 END) / COUNT(*), 2) AS taxa_retencao_percentual
FROM aluno a
GROUP BY 1
ORDER BY 1;
    """,
    48: """
SELECT
  c.nome_curso,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 0 ELSE 1 END) AS total_cotistas,
  ROUND(
    100.0 * SUM(CASE WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 0 ELSE 1 END) / COUNT(*),
    2
  ) AS percentual_cotistas
FROM aluno a
JOIN curso c ON c.id_curso = a.id_curso
GROUP BY c.nome_curso
ORDER BY percentual_cotistas DESC, c.nome_curso;
    """,
    49: """
SELECT
  CASE
    WHEN COALESCE(NULLIF(TRIM(a.cotas), ''), 'NAO') IN ('NAO', 'NÃO', 'N', '0') THEN 'Ampla concorrência / não cotista'
    ELSE 'Cotista'
  END AS grupo_ingresso,
  COUNT(*) AS total_alunos,
  SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) AS total_evadiu,
  ROUND(100.0 * SUM(CASE WHEN a.situacao IN ('MATRICULADO', 'CONCLUIDO') THEN 0 ELSE 1 END) / COUNT(*), 2) AS taxa_evasao_percentual
FROM aluno a
GROUP BY 1
ORDER BY taxa_evasao_percentual DESC;
    """,
    50: """
SELECT
  'NÃO SUPORTADA PELO SCHEMA ATUAL' AS status,
  'Não existem fatores socioeconômicos estruturados no schema atual' AS detalhe;
    """,
}
