import java.util.List;
import java.util.ArrayList;

class ProteinTranslator {

    List<String> translate(String rnaSequence) {
        ArrayList<String> listaSecuencias = new ArrayList<>();
        int longitudSegmento = 3;

        for (int i = 0; i < rnaSequence.length(); i += longitudSegmento) {
            if (i + longitudSegmento > rnaSequence.length()) {
                throw new IllegalArgumentException("Invalid codon");
            } else {
                String single_strand = rnaSequence.substring(i, i + longitudSegmento);

                switch (single_strand) {
                    case "AUG":
                        listaSecuencias.add("Methionine");
                        break;
                    case "UUU":
                    case "UUC":
                        listaSecuencias.add("Phenylalanine");
                        break;
                    case "UUA":
                    case "UUG":
                        listaSecuencias.add("Leucine");
                        break;
                    case "UCU":
                    case "UCC":
                    case "UCA":
                    case "UCG":
                        listaSecuencias.add("Serine");
                        break;
                    case "UAU":
                    case "UAC":
                        listaSecuencias.add("Tyrosine");
                        break;                    
                    case "UGU":                   
                    case "UGC":
                        listaSecuencias.add("Cysteine");
                        break;                      
                    case "UGG":
                        listaSecuencias.add("Tryptophan");
                        break;
                    case "UAA":
                    case "UAG":
                    case "UGA":
                        i += rnaSequence.length();
                        break;
                    default:
                        i += rnaSequence.length();
                        throw new IllegalArgumentException("Invalid codon");
                }
            }

        }
        List<String> lista = listaSecuencias;
        return lista;
    }
}
