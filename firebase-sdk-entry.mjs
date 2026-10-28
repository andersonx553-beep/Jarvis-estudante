/* Entrada do SDK instalada por npm e empacotada com o cliente. Sem imports de CDN. */
import {initializeApp} from 'firebase/app';
import {getAuth,connectAuthEmulator,setPersistence,browserLocalPersistence,onAuthStateChanged,signInWithEmailAndPassword,createUserWithEmailAndPassword,sendPasswordResetEmail,signOut,sendEmailVerification} from 'firebase/auth';
import {initializeFirestore,memoryLocalCache,connectFirestoreEmulator,collection,doc,orderBy,documentId,startAfter,Timestamp,limit,getDocsFromServer,query,runTransaction,serverTimestamp,getDocFromServer,setDoc} from 'firebase/firestore';
export const A={initializeApp};
export const H={getAuth,connectAuthEmulator,setPersistence,browserLocalPersistence,onAuthStateChanged,signInWithEmailAndPassword,createUserWithEmailAndPassword,sendPasswordResetEmail,signOut,sendEmailVerification};
export const F={initializeFirestore,memoryLocalCache,connectFirestoreEmulator,collection,doc,orderBy,documentId,startAfter,Timestamp,limit,getDocsFromServer,query,runTransaction,serverTimestamp,getDocFromServer,setDoc};
